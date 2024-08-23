# Implementing pressure curves



<figure><img src="../../.gitbook/assets/Slide_20240722_141622 (1).jpg" alt=""><figcaption></figcaption></figure>

Ultimately a pressure curve is a mathematical function that takes input logical pressure (p) and returns an output logical pressure (p’)

that is it maps logical pressure to logical pressure. The logical pressure comes in as a value between zero and one, and the output is a logical pressure between zero and one. The specifics of the mapping of the input to the output are completely arbitrary and we can make pressure curves do whatever we want.

<figure><img src="../../.gitbook/assets/Slide_20240722_141702.jpg" alt=""><figcaption></figcaption></figure>

In reality we wouldn't just have one pressure curve function with a single input logical pressure parameter like that. More typically we'd have a pressure curve function that accepts multiple parameters. By tweaking these additional parameters we can control what the pressure curve is actually doing in a dynamic way.
