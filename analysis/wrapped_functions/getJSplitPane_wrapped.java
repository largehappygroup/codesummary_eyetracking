public class SplitPaneParser {

    private JSplitPane jSplitPane;

    public JSplitPane getJSplitPane() {
        if (jSplitPane == null) {
            jSplitPane = new JSplitPane();

            DevicesTreePanel p = new DevicesTreePanel();
            p.addSelectionChangeListener(this);
            jSplitPane.setLeftComponent(p);
            jSplitPane.setRightComponent(getJTabbedPane());

            jSplitPane.setDividerSize(5);
            jSplitPane.setDividerLocation(200);
        }
        return jSplitPane;
    }

    private JTabbedPane getJTabbedPane() {
        // implementation logic for getting JTabbedPane
    }
}