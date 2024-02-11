#include <stdio.h>
#include <stdlib.h>

typedef struct listint_t 
{
    int data;
    struct listint_t *next;
}listint_t;
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
    {
        return (1);
    }
     listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;
 while (fast != NULL && fast->next != NULL)
 {
        fast = fast->next->next;

        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }
 if (fast != NULL)
 {
        slow = slow->next;
    }
 while (slow != NULL)
 {
        if (slow->data != prev->data)
	{
            return (0);
        }
        slow = slow->next;
        prev = prev->next;
    }
 return (1);
}
