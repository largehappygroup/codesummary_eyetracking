public class EntityRemover {
    
    public void removeSelection(IEntity selection) {
        if (selection == null) {
            String msg = "Argument 'selection' cannot be null.";
            throw new IllegalArgumentException(msg);
        }
        
        entitySel.remove(selection.getEntityId());
        if (selection.getType().equals(EntityType.MEMBER)) {
            memberCount--;
        } else {
            groupCount--;
        }
    }
}