# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554091384.0074508
_enable_loop = True
_template_filename = 'themes/custom/templates/pagination_helper.tmpl'
_template_uri = 'pagination_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['page_navigation']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_navigation(context,current_page,page_links,prevlink,nextlink,prev_next_links_reversed,surrounding=5):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs = context.get('abs', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="page-navigation">\n')
        for i, link in enumerate(page_links):
            if abs(i - current_page) <= surrounding or i == 0 or i == len(page_links) - 1:
                if i == current_page:
                    __M_writer('        <span class="current-page">')
                    __M_writer(str(i+1))
                    __M_writer('</span>\n')
                else:
                    __M_writer('        <a href="')
                    __M_writer(str(page_links[i]))
                    __M_writer('">')
                    __M_writer(str(i+1))
                    __M_writer('</a>\n')
            elif i == current_page - surrounding - 1 or i == current_page + surrounding + 1:
                __M_writer('      <span class="ellipsis">…</span>\n')
        __M_writer('</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/custom/templates/pagination_helper.tmpl", "uri": "pagination_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 16, "27": 2, "34": 2, "35": 4, "36": 5, "37": 6, "38": 7, "39": 7, "40": 7, "41": 8, "42": 9, "43": 9, "44": 9, "45": 9, "46": 9, "47": 11, "48": 12, "49": 15, "55": 49}}
__M_END_METADATA
"""
