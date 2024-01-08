#include <Python.h>

/**
 * print_python_list_info - Print basic information about Python lists
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int len, alloced, i;
	PyObject *py_obj;

	len = Py_SIZE(p);
	alloced = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", alloced);

	for (i = 0; i < len; i++)
	{
		py_obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(py_obj)->tp_name);
	}
}
