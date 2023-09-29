public class Exporter {
    public void exportXVRL( XMLStreamWriter xvrLDoc ) throws Exception{
        JAXBContext context = JAXBContext.newInstance( ValidationReport.class );
        Marshaller m = context.createMarshaller();
        m.setProperty( Marshaller.JAXB_FORMATTED_OUTPUT, true );
        ValidationReport vReport = exportVReport();

        if ( vReport != null ) m.marshal( vReport, xvrLDoc );
    }
}