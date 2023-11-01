#ifndef LISTS_H
#include "lists.h"
#define LISTS_H
#endif
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list{
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fp = list->next->next, *sp = list->next;
	int res = 0;


	while (sp != NULL)
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
