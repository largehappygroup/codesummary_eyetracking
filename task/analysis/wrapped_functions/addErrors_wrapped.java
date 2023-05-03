public class ErrorManager {
  
  public void addErrors( String el, IErrorDescription... error ) {
    final IErrorDescription[] msg = errors.get( el );
    // we expect that the main scenario is to add only once errors per property...
    errors.put( el, msg == null ? error : merge( msg, error ));
  }
  
}