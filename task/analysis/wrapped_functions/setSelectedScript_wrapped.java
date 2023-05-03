public class MyClass {

    public void setSelectedScript( Object script ) {
        Object selectedScript = script;

        // expand to and select the specified container
        List<Object> itemsToExpand = new ArrayList<>();
        IContainer parent = project.getParent();
        while ( parent != null ) {
            itemsToExpand.add( 0, parent );
            parent = parent.getParent();
        }
        treeViewer.setExpandedElements( itemsToExpand.toArray() );
        treeViewer.setSelection( new StructuredSelection( project ), true );
    }
}