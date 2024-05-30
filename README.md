# mdx_convo

Markdown extension for displaying message conversations.

# Showcase

The following markup..

> <convo>
  < Obi-Wan never told you what happened to your father
  > He told me enough! He told me YOU killed him!
  < No, I am your father!
  > NOOOOOOOOOOOOOOOOOOO
  </convo>

Results in..

<div class="mdx-convo">
<div class="mdx-convo-speech-left">Obi-Wan never told you what happened to your father</div>
<div class="mdx-convo-speech-right">He told me enough! He told me YOU killed him!</div>
<div class="mdx-convo-speech-left">No, I am your father!</div>
<div class="mdx-convo-speech-right">NOOOOOOOOOOOOOOOOOOO</div>
</div>

And could be styled like..

![Message conversation example](example.png)


## Example usage

```python
import markdown
import markdown_inline_convo

md = markdown.Markdown(
	extensions = [
		markdown_inline_convo.makeExtension()
	]
)

return md.convert(<string>)
```
