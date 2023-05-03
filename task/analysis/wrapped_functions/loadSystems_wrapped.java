public class SystemLoader {
    private JComboBox<String> systemCombo;
    private CopyBookInterface copyBookInterface;
    private ArrayList<SystemItem> systems;
    private JTextArea message;
    private boolean dbLink;

    public void loadSystems() {
        int i, num;
        SystemItem dtls;
        systemCombo.removeAllItems();
        systemCombo.addItem("<All>");

        dbLink = true;
        try {
            systems = copyBookInterface.getSystems();
        } catch (Exception ex) {
            if (message != null) {
                message.setText(ex.getMessage());
                message.setCaretPosition(1);
            }
            ex.printStackTrace();
            systems = new ArrayList<SystemItem>();
            dbLink = false;
        }
        num = systems.size();

        for (i = 0; i < num; i++) {
            dtls = systems.get(i);
            systemCombo.addItem(dtls.description);
        }
    }
}