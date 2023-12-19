#include <Python.h>

/**
 * print_python_list - function that print python list
 * @p: pointer to pyobject
 */

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
		if (PyBytes_Check(element))
			print_python_bytes(element);
		else if (PyList_Check(element))
			print_python_list(element);
		else if (PyTuple_Check(element))
			print_python_tuple(element);
		else if (PyFloat_Check(element))
			print_python_float(element);
		else if (PyLong_Check(element))
			print_python_int(element);
		else if (PyUnicode_Check(element))
			print_python_str(element);
	}
}

/**
 * print_python_bytes - function that print bytes
 * @p: pointer to pyobject
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;
	char *str;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);

	str = PyBytes_AsString(p);

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  trying string: %s\n", str);
	printf("  first 10 bytes: ");

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < size - 1)
			printf(" ");
	}

	printf("\n");
}

/**
 * print_python_float - function that print float
 * @p: pointer to pyobject
*/
void print_python_float(PyObject *p)
{
	PyFloatObject *f = (PyFloatObject *)p;
	double value = f->ob_fval;

	printf("[.] float object info\n");
	printf("  value: %f\n", value);

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
}

/**
 * main - main function
 * Return: 0
*/
int main(void)
{
	Py_Initialize();
	Py_Finalize();
	return (0);
}
