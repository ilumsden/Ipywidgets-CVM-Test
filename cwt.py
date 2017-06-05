import ipywidgets as ipyw
from traitlets import Unicode
from IPython.display import HTML, display

class HelloWidget(ipyw.DOMWidget):
    _view_name = Unicode("HelloView").tag(sync=True)
    _view_module = Unicode("hello").tag(sync=True)
    value = Unicode("Hello World").tag(sync=True)

%%javascipt
require.undef("hello");

define("hello", ["jupyter-js-widgets"], function(widgets) {
    var HellowView = widgets.DOMWidgetView.extend({
        render: function() {
            this.el.textContent = this.model.get("value");
        },
    });
    return {
        HelloView : HelloView
    };
});
