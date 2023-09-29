public class MyClass {
    
    public Node setNamedItem( Node arg ) {
        try {
            return NodeImpl.build( XMLParserImpl.setNamedItem( this.getJsObject(),
            (( DOMItem ) arg ).getJsObject() ));
        } catch ( JavaScriptException e ) {
            throw new DOMNodeException( DOMNodeException.INVALID_MODIFICATION_ERR, e, this );
        }
    }
    
}