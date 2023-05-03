class ClassName {
  
  public void testGetClassification() {
    System.out.println( "getClassification" );
    SystemClient_DBImpl instance = new SystemClient_DBImpl();
        
    Set expResult = null;
    Set result = instance.getClassification();
    assertEquals( expResult, result );
        
    // TODO review the generated test code and remove the default call to fail.
    fail( "The test case is a prototype." );
  } 
  
}