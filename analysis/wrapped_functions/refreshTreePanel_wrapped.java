public class TreePanelRefresh {
    public void refreshTreePanel() {
        DefaultMutableTreeNode root = new DefaultMutableTreeNode( "ALL" );
        DefaultTreeModel treeModel = new DefaultTreeModel( root );
        tree.setModel( treeModel );
        tree.setBounds( new Rectangle( 0, 0, 196, 443 ));
        tree.setLayout( null );
        tree.setBackground( Color.white );
        tree.setCellRenderer( new UserIconRenderer() );

        addAllUsers();

        TreePath treePath = tree.getPathForRow( 0 );
        tree.fireTreeExpanded( treePath );
    }
}