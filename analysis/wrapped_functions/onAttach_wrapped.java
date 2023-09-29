public class Widget {

    protected void onAttach() {
        if ( attached )
            return;
        
        attached = true;
        
        // Set the main element's event listener. This should only be set
        // while the widget is attached, because it creates a circular
        // reference between JavaScript and the DOM.
        DOM.setEventListener( getElement(), this );
        
        // Now that the widget is attached, call onLoad().
        onLoad();
    }
    
}