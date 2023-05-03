class MyClass {
    private void jbInit() throws Exception {
        setLayout( new GridBagLayout() );

        add( m_environmentpanel,
            new GridBagConstraints( 0, 0, 1, 1, 1.0, 1.0,
                              GridBagConstraints.CENTER,
                              GridBagConstraints.HORIZONTAL,
                              new Insets( 0, 0, 0, 0 ), 0, 0 ));
    }
}