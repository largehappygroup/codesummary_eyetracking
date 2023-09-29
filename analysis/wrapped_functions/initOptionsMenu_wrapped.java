public class MenuInitializer {
    private JMenu optionsMenu;

    public void initOptionsMenu(JMenuBar bar) {
        optionsMenu = new JMenu("Options");
        optionsMenu.setToolTipText("Options for SWGAide");
        optionsMenu.setMnemonic(KeyEvent.VK_O);

        optionsMenu.add(optionsSWGCraftMenuItem());
        optionsMenu.setEnabled(true);
        bar.add(optionsMenu);
    }

    private JMenuItem optionsSWGCraftMenuItem() {
        // implementation goes here
    }
}