public class PrintFunctionWrapper {
    public String print( String tab ) {
        if ( content instanceof RegExp ) {
            return tab + "type = " + type + Out.NL + tab + "content :" + Out.NL + ((RegExp)content).print( tab+"  " );
        }
        else
            return tab + "type = " + type + Out.NL + tab + "content :" + Out.NL + tab + "  " + content;
    }
}