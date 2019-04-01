# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554091637.1512341
_enable_loop = True
_template_filename = 'themes/custom/templates/require_helper.tmpl'
_template_uri = 'require_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['require_script', 'require_script_ifpost', 'require_script_ifposts']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_require_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n  <script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.5/require.min.js" async crossorigin="anonymous"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_require_script_ifpost(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        def require_script():
            return render_require_script(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags and 'require' in post.tags:
            __M_writer('    ')
            __M_writer(str(require_script()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_require_script_ifposts(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        def require_script():
            return render_require_script(context)
        any = context.get('any', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if any((post.tags and 'require' in post.tags) for post in posts):
            __M_writer('    ')
            __M_writer(str(require_script()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/require_helper.tmpl", "uri": "require_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 3, "22": 9, "23": 16, "29": 1, "33": 1, "39": 5, "45": 5, "46": 6, "47": 7, "48": 7, "49": 7, "55": 12, "63": 12, "64": 13, "65": 14, "66": 14, "67": 14, "73": 67}}
__M_END_METADATA
"""
