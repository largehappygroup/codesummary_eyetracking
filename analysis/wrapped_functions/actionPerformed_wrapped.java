public class SomeClass {
    public void actionPerformed( ActionEvent e ) {
        int[] selectedRows = features.getSelectedRows();

        if ( selectedRows.length > 0 ) {
            boolean valueToBeSet = (( Boolean ) features.getValueAt(
                selectedRows[ 0 ], 0 )).booleanValue();

            for ( int i = 0; i < selectedRows.length; ++i ) {
                features.setValueAt( new Boolean( !valueToBeSet ), selectedRows[ i ], 0 );
            }
        }
    }
}