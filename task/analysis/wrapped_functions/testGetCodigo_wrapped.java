public class CronogramaTest {
    public void testGetCodigo() {
        System.out.println( "getCodigo" );
            
        Cronograma instance = null;   
        String expResult = "";
        String result = instance.getCodigo();
        assertEquals( expResult, result );
            
        // TODO review the generated test code and remove the default call to fail.
        fail( "The test case is a prototype." );
    }
}