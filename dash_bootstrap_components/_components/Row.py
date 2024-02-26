# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Row(Component):
    """A Row component.
Row is one of the core layout components in Bootstrap. Build up your layout
as a series of rows of columns. Row has arguments for controlling the
vertical and horizontal alignment of its children, as well as the spacing
between columns.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- align (a value equal to: 'start', 'center', 'end', 'stretch', 'baseline'; optional):
    Set vertical alignment of columns in this row. Options are
    'start', 'center', 'end', 'stretch' and 'baseline'.

- className (string; optional):
    **DEPRECATED** Use `class_name` instead.  Often used with CSS to
    style elements with common properties.

- class_name (string; optional):
    Often used with CSS to style elements with common properties.

- justify (a value equal to: 'start', 'center', 'end', 'around', 'between', 'evenly'; optional):
    Set horizontal spacing and alignment of columns in this row.
    Options are 'start', 'center', 'end', 'around' and 'between'.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components See
    https://reactjs.org/docs/lists-and-keys.html for more info.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- style (dict; optional):
    Defines CSS styles which will override styles previously set."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_bootstrap_components'
    _type = 'Row'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, style=Component.UNDEFINED, class_name=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, align=Component.UNDEFINED, justify=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'align', 'className', 'class_name', 'justify', 'key', 'loading_state', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'align', 'className', 'class_name', 'justify', 'key', 'loading_state', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Row, self).__init__(children=children, **args)
