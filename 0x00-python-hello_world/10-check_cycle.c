#include "lists.h"
/**
 * check_cycle - checks for cycle in a linked list
 * @list: linked list to check
 * Return: 1 if cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *list1, *list2;

	if (list == NULL || list->next == NULL)
		return (0);

	list1 = list->next;
	list2 = list->next->next;

	while (list1 && list2 && list2->next)
	{
		if (list1 == list2)
			return (1);

		list1 = list1->next;
		list2 = list2->next->next;
	}

	return (0);
}
