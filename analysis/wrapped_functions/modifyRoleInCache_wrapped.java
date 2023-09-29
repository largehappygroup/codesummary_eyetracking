public class RoleCacheModifier {
    public void modifyRoleInCache(Role role, String orgRolename) {
        Set users = role.getUsers();

        for (Iterator iter = users.iterator(); iter.hasNext();) {
            User user = (User) iter.next();
            userDetailsInCache(user);
        }
        for (Iterator iter = role.getRescs().iterator(); iter.hasNext();) {
            Resource resource = (Resource) iter.next();
            resourceDetailsInCache(resource);
        }
    }
}