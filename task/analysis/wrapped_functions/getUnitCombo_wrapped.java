public class UnitForm {
    private JComboBox m_UnitCombo;
    private FreeParameter m_FreePara;
    
    public UnitForm() {
        m_FreePara = new FreeParameter();
    }

    private JComboBox getUnitCombo() {
        if ( m_UnitCombo == null ) {
            m_UnitCombo = new JComboBox();
            m_UnitCombo.setBounds( 87, 83, 125, 22 );
            m_UnitCombo.setModel( getUnitComboModel() );
        }
        if ( m_FreePara.getUnit() != null ) {
            m_UnitCombo.setSelectedItem( m_FreePara.getUnit() );
        }
        return m_UnitCombo;
    }

    private DefaultComboBoxModel getUnitComboModel() {
        DefaultComboBoxModel result = new DefaultComboBoxModel();
        result.addElement( "Meter" );
        result.addElement( "Foot" );
        return result;
    }
}