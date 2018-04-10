# html-parser

Simple HTML parser, sample output:

```js
[{
    'DOCTYPE': {}
}, {
    'html': {
        'children': [{
            'head': {
                'children': [{
                    'meta': {
                        'charset': '"UTF-8"'
                    }
                }, {
                    'title': {
                        'content': 'Document'
                    }
                }, {
                    'script': {
                        'content': '\n        var x = "<p>test</p>";\n    '
                    }
                }]
            }
        }],
        'lang': '"en"'
    }
}, {
    'body': {
        'children': [{
            'div': {
                'children': [{
                    'p': {
                        'content': 'This is p tag'
                    }
                }]
            }
        }]
    }
}]
```
