public class MyClass {

    public List getAll(Object key) {
        Object value = mMap.get(key);

        if (value instanceof List) {
            return ((List) value);
        } else {
            List list = new ArrayList();

            if (value != null || mMap.containsKey(key)) {
                list.add(value);
            }
            mMap.put(key, list);

            return list;
        }
    }
}