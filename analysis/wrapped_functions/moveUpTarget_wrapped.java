public class MoveUpTarget {

    public void moveUpTarget( int index ) {
        Object target= targets.get( index );

        if ( index == 0 || target == null ) {
            return;
        }
        targets.set( index, targets.get( index - 1 ));
        targets.set( index - 1, target );
        log.debug( "New ordering" );

        for ( int i = 0; i < targets.size(); i++ ) {
            log.debug( "|t" + i + targets.get( i ));
        }
    }
    
}