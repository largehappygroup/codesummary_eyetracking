public class MyClass {

    public void swapItems( int index, int change ){
        if( index >= 0 && index < allItems.length && change >= 0 && change < allItems.length ){
            MenuItem temp = allItems[ index ];
            allItems[ index ] = allItems[ change ];
            allItems[ change ] = temp;
        }
    }

}