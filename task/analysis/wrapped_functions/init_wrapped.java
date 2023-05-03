public class MyClass {
    private Map<String, Object> _innerData;
    private ListModel<Object> _srcModel;
    private ListDataListener _srcListener;

    public void init() {
        _innerData = Collections.synchronizedMap(new LinkedHashMap<String, Object>());
        Iterator<Entry<String, Object>> itr = _srcModel.entrySet().iterator();

        while (itr.hasNext()) {
            Entry<String, Object> entry = itr.next();
            _innerData.put(entry.getKey(), entry.getValue());
        }

        _srcListener = new ListDataListener() {
            public void onChange(ListDataEvent event) {
                onListDataChange(event);
            }
        };
        
        _srcModel.addListDataListener(_srcListener);
    }

    private void onListDataChange(ListDataEvent event) {
        // do something on list data change
    }
}