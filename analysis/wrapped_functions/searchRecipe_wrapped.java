public class RecipeSearcher {
    
    private Recipe searchRecipe ( Recipe re ) {	
        Recipe recipe;
    		
        for ( IngredientAmount iam : re.getIngredients() ) {
            if ( iam.getFood() instanceof Recipe ) {
                if (( Recipe )iam.getFood() == m_ActiveRecipe ) {
                    return re;
                } else {
                    recipe = searchRecipe (( Recipe ) iam.getFood());
    					
                    if ( recipe != null ) {
                        return recipe;
                    }
                }
            }			
        }		
        return null;
    }
    
}