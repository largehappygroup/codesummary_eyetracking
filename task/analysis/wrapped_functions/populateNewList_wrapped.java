public class ResourceList {
    private ArrayList<Wrapper> newResources;
    private DefaultListModel<Wrapper> newListModel;

    public ResourceList() {
        // constructor code here
    }

    private void populateNewList() {
        newResources = mergeNewResources();
        SwingUtilities.invokeLater( new Runnable() {
            @SuppressWarnings( "synthetic-access" )
            @Override
            public void run() {
                newListModel.clear();
                for ( Wrapper wr : newResources )
                    newListModel.addElement( wr );
            }
        });
    }

    private ArrayList<Wrapper> mergeNewResources() {
        // merge code here
    }
}