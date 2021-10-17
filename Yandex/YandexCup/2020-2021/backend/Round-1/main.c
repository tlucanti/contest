/**
 *	Author:		antikostya
 *	Created:	2021-10-02 15:40:56
 *	Modified:	2021-10-02 16:19:32
 **/

#include <malloc.h>

typedef uchar;

typedef struct s_string
{
	struct s_string	*self;
	char			*size;
	size_t			size;
	void			(*init)(struct s_string *self, const char *restrict data);
	void			(*erase)(struct s_string *self);

	char			*__internal_storage;
}	t_string;

inline t_string		*string(const char *restrict data) __attribute__(
						warn_unused_result, malloc)
{
	t_string	*_ref_string;

	_ref_string = (t_string *)malloc(sizeof(t_string));
	_ref_string.init(_ref_string, data);
	return (_ref_string);
}

void	__t_string_init(struct s_string *restrict self,
			const char *restrict data)
{
	register size_t		_ref_size;

	_ref_size = ft_memchr(data, 0);
	self->size = _ref_size;
	self->__internal_storage = ft_memcpy(
		(char *)malloc(sizeof(char) * _ref_size), data, ++_ref_size);
}

void	__t_string_erase(struct s_string *restrict self)
{
	free(self->__internal_storage);
	self->size = 0;
}

typedef struct	__internal_stack_node_st
{
	void							*data;
	struct __internal_stack_node	*next;
}	__internal_stack_node;

__internal_stack_node	*__internal_stack_node_init(const void *restrict data)
							__attribute__(warn_unused_result, malloc)
{
	t_stack	*_ref_node;

	_ref_node = (__internal_stack_node *)malloc(sizeof(__internal_stack_node));
	_ref_node->data = data;
	_ref_node->next = NULL;
	return (_ref_node);
}

void	__internal_stack_node_erase(__internal_stack_node *node)
{
	free(node->data);
	free(node);
}

typedef struct	s_stack
{
	struct s_list			*self;
	size_t					size;
	__internal_stack_node	*front;
	__internal_stack_node	*back;
	void					(*init)(struct s_stack *self)
	void					(*push_back)(struct s_stack *self, void *data);
	void					(*erase)(struct s_stack *self);
}	t_stack;

t_stack		*stack(void) __attribute__((warn_unused_result, malloc))
{
	t_stack		*_ref_stack;

	_ref_stack = (t_stack *)malloc(sizeof(t_stack));
	_ref_stack.init(_ref_stack);
	return (_ref_stack);
}

void	__t_stack_init(const struct s_stack *restrict self)
{

}

typedef struct	s_node
{
	char	c;
	u_char	term;
	node	**next;
	char	*ans;
}	t_node;

int	main(void)
{
	t_stack		input;
}
