public class ResetSchedConflict {

    public void resetSchedConflict() {
        try {
            if ( listData == null || listData.size() == 0 )
                return;
            for ( int i = 0;  i < listData.size();  i++ ) {
                TblAuditor auditor = ( TblAuditor ) listData.get( i );
                auditor.setSchedConflict( false );
            }
        } catch ( Exception ex ) {
            logger.error( ex );
            FacesUtils.addErrorMessage( ex.getMessage() );
        }
    }
    
}