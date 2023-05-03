public class MenuOptions {
    private void addLimit( JPopupMenu popup ) {
        JMenuItem limit = makeMenuItem( "Write option: Limit days...","
                                   Specify a limit for the written output, in days",
                                   new ActionListener() {
                                       @SuppressWarnings( "synthetic-access" )
                                       @Override
                                       public void actionPerformed( ActionEvent e ) {
                                           actionLimit();
                                       }
                                   });
        popup.add( limit );
    }

    private JMenuItem makeMenuItem(String s, String s1, ActionListener actionListener) {
        return new JMenuItem(s);
    }

    private void actionLimit() {
        // do something
    }
}