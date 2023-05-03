public class FunctionWrapper {

    public Value evaluate( Value value ) throws ExternalFunctionException {
        if (!( value instanceof Literal )) {
            throw new ExternalFunctionException( "Values need to be literals to be understood" );
        }    
        DateTime date = this.converter.convertDateTime(( Literal ) value );
        
        return this.converter.convertInteger( date.getHour() );
    }
    
}