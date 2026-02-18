using System.Text.RegularExpressions;

var rootDir = ParseArg(args, "--root");
var outputFile = ParseArg(args, "--output");

if (string.IsNullOrEmpty(rootDir))
{
    // Try to find root by looking for SUMMARY.md in current or parent directories
    var current = new DirectoryInfo(Directory.GetCurrentDirectory());
    while (current != null)
    {
        if (File.Exists(Path.Combine(current.FullName, "SUMMARY.md")))
        {
            rootDir = current.FullName;
            break;
        }
        current = current.Parent;
    }
}

if (string.IsNullOrEmpty(rootDir))
{
    Console.WriteLine("Error: Could not determine repository root. Please use --root.");
    return;
}

if (string.IsNullOrEmpty(outputFile))
{
    outputFile = Path.Combine(rootDir, "scripts-output", "pages_list.txt");
}

ListPages(rootDir, outputFile);

static string? ParseArg(string[] args, string key)
{
    for (int i = 0; i < args.Length - 1; i++)
    {
        if (args[i] == key) return args[i + 1];
    }
    return null;
}

static void ListPages(string rootDir, string outputFile)
{
    var summaryPath = Path.Combine(rootDir, "SUMMARY.md");
    if (!File.Exists(summaryPath))
    {
        Console.WriteLine($"Error: SUMMARY.md not found at {summaryPath}");
        return;
    }

    var pages = new List<string>();
    var pageTitles = new Dictionary<string, string>();
    var backlinks = new Dictionary<string, List<(string Source, string Text)>>();

    // Regex for [text](link)
    var linkPattern = new Regex(@"\[(.*?)\]\((.*?)\)");

    // 1. Get Master List from SUMMARY.md
    try
    {
        foreach (var line in File.ReadLines(summaryPath))
        {
            var cleanLink = ExtractLink(line, linkPattern);
            if (!string.IsNullOrEmpty(cleanLink))
            {
                pages.Add(cleanLink);
                if (!backlinks.ContainsKey(cleanLink))
                {
                    backlinks[cleanLink] = new List<(string, string)>();
                }
            }
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Error reading SUMMARY.md: {ex.Message}");
        return;
    }

    Console.WriteLine($"Found {pages.Count} pages in SUMMARY.md. Analyzing backlinks...");

    // 2. Analyze each page
    foreach (var pagePath in pages)
    {
        var relativePath = pagePath;
        var inputs = new[] { relativePath };
        
        // Handle directory links by trying README.md
        var fullPath = Path.Combine(rootDir, relativePath);
        if (Directory.Exists(fullPath))
        {
            fullPath = Path.Combine(fullPath, "README.md");
        }

        if (File.Exists(fullPath))
        {
            try
            {
                var lines = File.ReadAllLines(fullPath);
                
                // Get Title
                string title = "Unknown Title";
                foreach (var line in lines)
                {
                    if (line.TrimStart().StartsWith("# "))
                    {
                        title = line.TrimStart().Substring(2).Trim();
                        break;
                    }
                }
                pageTitles[relativePath] = title;

                // Find outgoing links
                foreach (var line in lines)
                {
                    var matches = linkPattern.Matches(line);
                    foreach (Match match in matches)
                    {
                        var text = match.Groups[1].Value;
                        var link = match.Groups[2].Value;
                        
                        // cleanup link
                        if (link.Contains(" \"")) link = link.Split(new[] { " \"" }, StringSplitOptions.None)[0];
                        else if (link.Contains(' ')) link = link.Split(' ')[0];
                        
                        link = link.Trim();
                        
                        // Ignore non-md or external
                        if (link.StartsWith("http") || link.StartsWith("mailto:") || link.StartsWith("#")) continue;
                        
                        // Remove anchors/query
                        link = link.Split('#')[0].Split('?')[0];
                        
                        if (!link.EndsWith(".md", StringComparison.OrdinalIgnoreCase) && !link.EndsWith("/")) 
                        {
                            // naive check for extensionless files or assumed directories? 
                            // Markdown usually links to .md or directories.
                            // Let's only track .md links or obvious directory links that might match our pages.
                            if (!string.IsNullOrEmpty(Path.GetExtension(link))) continue; 
                        }

                        // Resolve path relative to current file
                        // Current file directory relative to root
                        var currentDir = Path.GetDirectoryName(relativePath) ?? "";
                        var targetPath = Path.GetFullPath(Path.Combine(rootDir, currentDir, link));
                        
                        // Convert back to relative path from root
                         var targetRelative = Path.GetRelativePath(rootDir, targetPath).Replace('\\', '/');
                        
                        // Normalize directory links to remove trailing slash for matching
                        if (targetRelative.EndsWith("/")) targetRelative = targetRelative.TrimEnd('/');
                        
                        // If we map this to our known pages
                        if (backlinks.ContainsKey(targetRelative))
                        {
                            backlinks[targetRelative].Add((relativePath, text));
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                // Console.WriteLine($"Error processing {relativePath}: {ex.Message}");
                pageTitles[relativePath] = "Error reading file";
            }
        }
        else
        {
            pageTitles[relativePath] = "File not found";
        }
    }

    // 3. Write Output
    var outputLines = new List<string>();
    foreach (var page in pages)
    {
        var title = pageTitles.ContainsKey(page) ? pageTitles[page] : "Unknown";
        outputLines.Add($"{page} - {title}");
        
        if (backlinks.ContainsKey(page) && backlinks[page].Count > 0)
        {
            outputLines.Add("  Used by:");
            foreach (var link in backlinks[page])
            {
                // limit text snippet length if needed, currently grabbing full link text
                outputLines.Add($"    - {link.Source} ({link.Text})");
            }
        }
    }

    var outDir = Path.GetDirectoryName(outputFile);
    if (!string.IsNullOrEmpty(outDir))
    {
        Directory.CreateDirectory(outDir);
    }

    File.WriteAllLines(outputFile, outputLines);
    Console.WriteLine($"List written to {outputFile}");
}

static string? ExtractLink(string line, Regex pattern)
{
    var match = pattern.Match(line);
    if (match.Success)
    {
        var rawLink = match.Groups[2].Value; // Group 2 is the url part in existing regex logic? 
        // Wait, caller used logic: [text](link) -> Group 1 is text, Group 2 is link in my new regex above?
        // Actually my new regex is `\[(.*?)\]\((.*?)\)`
        // Group 1: text
        // Group 2: link
        
        // However, the ORIGINAL code logic in `ListPages` (previous version) had its own parsing logic 
        // which I am replacing. I need to be careful with the helper extraction logic for SUMMARY.md 
        // vs the general file one.
        
        var cleanLink = rawLink.Trim();
        if (cleanLink.StartsWith('<') && cleanLink.EndsWith('>')) cleanLink = cleanLink[1..^1];
        if (cleanLink.Contains(" \"")) cleanLink = cleanLink.Split(new[] { " \"" }, StringSplitOptions.None)[0];
        else if (cleanLink.Contains(' ')) cleanLink = cleanLink.Split(' ')[0];
        
        cleanLink = cleanLink.Trim();
        
        if (cleanLink.StartsWith("http") || cleanLink.StartsWith("ftp") || cleanLink.StartsWith("mailto:")) return null;
        
        return cleanLink.Split('#')[0].Split('?')[0];
    }
    return null;
}
