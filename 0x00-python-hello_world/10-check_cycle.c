#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list{
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fp, *sp;
	int res = 0;

	if (list == NULL || list->next == NULL)
		return (0);

	fp = list->next, sp = list;

	while (fp != NULL)
	{
		if (sp == fp)
		{
			res = 1;
			break;
		}

		fp = fp->next->next, sp = sp->next;
	}

	return (res);
}
