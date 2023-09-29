public class CSSConditionalSelectorImpl {
    public boolean equals( Object obj ) {
        if ( obj == null || ( obj.getClass() != getClass() )) {
            return false;
        }
        CSSConditionalSelectorImpl s = ( CSSConditionalSelectorImpl ) obj;
        return ( s.simpleSelector.equals( simpleSelector ) && s.condition.equals( condition ));
    }
}