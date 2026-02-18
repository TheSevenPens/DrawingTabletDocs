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
    var linkPattern = new Regex(@"\[.*?\]\((.*?)\)");

    try
    {
        foreach (var line in File.ReadLines(summaryPath))
        {
            var match = linkPattern.Match(line);
            if (match.Success)
            {
                var rawLink = match.Groups[1].Value;
                var cleanLink = rawLink.Trim();

                if (cleanLink.StartsWith('<') && cleanLink.EndsWith('>'))
                {
                    cleanLink = cleanLink[1..^1];
                }

                // Remove title
                if (cleanLink.Contains(" \""))
                {
                    cleanLink = cleanLink.Split(new[] { " \"" }, StringSplitOptions.None)[0];
                }
                else if (cleanLink.Contains(" '"))
                {
                    cleanLink = cleanLink.Split(new[] { " '" }, StringSplitOptions.None)[0];
                }
                else if (cleanLink.Contains(' '))
                {
                        cleanLink = cleanLink.Split(' ')[0];
                }

                cleanLink = cleanLink.Trim();

                // Ignore external
                if (cleanLink.StartsWith("http:") || cleanLink.StartsWith("https:") || 
                    cleanLink.StartsWith("ftp:") || cleanLink.StartsWith("mailto:"))
                {
                    continue;
                }

                // Remove anchors and query params
                cleanLink = cleanLink.Split('#')[0].Split('?')[0];

                if (!string.IsNullOrEmpty(cleanLink))
                {
                    pages.Add(cleanLink);
                }
            }
        }

        Console.WriteLine($"Found {pages.Count} pages in SUMMARY.md.");

        var outDir = Path.GetDirectoryName(outputFile);
        if (!string.IsNullOrEmpty(outDir))
        {
            Directory.CreateDirectory(outDir);
        }

        File.WriteAllLines(outputFile, pages);
        Console.WriteLine($"List written to {outputFile}");

    }
    catch (Exception ex)
    {
        Console.WriteLine($"Error processing file: {ex.Message}");
    }
}
