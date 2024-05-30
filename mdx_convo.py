"""
Markup a message conversations with speech bubbles

The following:

<convo>
< Obi-Wan never told you what happened to your father
> He told me enough! He told me YOU killed him!
< No, I am your father!
> NOOOOOOOOOOOOOOOOOOO
</convo>

Results in:

<div class="mdx-convo">
<div class="mdx-convo-speech-left">Obi-Wan never told you what happened to your father</div>
<div class="mdx-convo-speech-right">He told me enough! He told me YOU killed him!</div>
<div class="mdx-convo-speech-left">No, I am your father!</div>
<div class="mdx-convo-speech-right">NOOOOOOOOOOOOOOOOOOO</div>
</div>
"""

import re
import markdown


class InlineConvoExtension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        """ Add InlineConvoPreprocessor to the Markdown instance. """
        md.registerExtension(self)
        md.preprocessors.add('convo', InlineConvoCompiler(md), "_begin")


class InlineConvoCompiler(markdown.preprocessors.Preprocessor):

    def __init__(self, md):
        super(InlineConvoCompiler, self).__init__(md)

    def run(self, lines):
        """ Match and generate convo html """

        CONVO_RE_QUESTION = re.compile(
            r'^<convo>\n(?P<msgs>.*?)</convo>$',
            re.MULTILINE | re.DOTALL
        )

        text = "\n".join(lines)

        while 1:
            m = CONVO_RE_QUESTION.search(text)
            html = ''
            if m:
                for msg in m.group('msgs').split('\n'):
                    if msg:
                        parsed_msg = msg.split(' ', 1)
                        prefix = parsed_msg[0]
                        content = parsed_msg[1]

                        match prefix:
                            case '<':
                                html += '<div class="mdx-convo-speech-left">' + content + '</div>\n'
                            case '>':
                                html += '<div class="mdx-convo-speech-right">' + content + '</div>\n'
                            case _:
                                html += msg + '\n'

                text = '%s\n%s\n%s' % (text[:m.start()], '<div class="mdx-convo">\n' + html + '</div>', text[m.end():])
            else:
                break

        return text.split("\n")


def makeExtension(*args, **kwargs):
    return InlineConvoExtension(*args, **kwargs)


