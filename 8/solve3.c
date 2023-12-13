#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>


struct node {
    int l;
    int r;
    int t;
};

int *indices;

int index_count = 0;

struct node nodes[1000];

char **lines;

char **keys;

int count = 0;

struct node ghosts[6];

int get_key_index(char *key) {
	for (int i = 0; i < count; i++) {
		if (strcmp(keys[i], key) ==0) {
			return i;
		}
	}
	printf("cant find index for key %s\n", key);
	exit(1);
}

struct node get_node(char *line) {

	struct node rn = {0, 0, 0};

	char *l = malloc((3 + 1) * sizeof(char));

	for (int i = 0, j = 7; j < 10; i++, j++) {
		l[i] = line[j];
	}
	l[3] = '\0';

	rn.l = get_key_index(l);

	for (int i = 0, j = 12; j < 15; i++, j++) {
		l[i] = line[j];
	}
	l[3] = '\0';

	rn.r = get_key_index(l);

	int t = 0;
	if (line[2] == 'A') {
		t = 1;
	}
	else if (line[2] == 'Z') {
		t = -1;
	}

	rn.t = t;

	return rn;
}

void parse_input(FILE *fp) {
	
	char *buffer = NULL;
	size_t len;

	ssize_t bytes_read = getline(&buffer, &len, fp);

	if (bytes_read != -1) {
		printf("index line: %s\n", buffer);
	}
	else {
		printf("didnt read index line\n");
		exit(1);
	}

	indices = malloc(sizeof(int) * bytes_read);

    index_count = 0;
	for (int i = 0; i < bytes_read; i++) {
		if (buffer[i] == 'L') {
			indices[i] = 0;
		}
		else if (buffer[i] == 'R') {
			indices[i] = 1;
		}
        else if (buffer[i] == '\n') {
            break;
        }
        index_count++;
	}

	bytes_read = getline(&buffer, &len, fp);

	if (bytes_read != -1) {
		printf("blank line: %s\n", buffer);
	}
	else {
		printf("didnt read blank line\n");
		exit(1);
	}

	lines = malloc(1000 * sizeof(char*));

	while (bytes_read != -1) {
		bytes_read = getline(&buffer, &len, fp);
		if (bytes_read != -1) {
			lines[count] = malloc((20 + 1) * sizeof(char)); // give line length 20
			strcpy(lines[count], buffer);
            count++;
		}

		if (count >= 1000) {
			printf("curently doing only 1000 nodes.. :(\n");
			exit(1);
		}
	}

	keys = malloc(1000 * sizeof(char*));

	for (int i = 0; i < count; i++) {
		keys[i] = malloc((3 + 1) * sizeof(char));
		strncpy(keys[i], lines[i], 3);
		keys[i][3] = '\0';
	}

	for (int i = 0; i < count; i++) {
		struct node n = get_node(lines[i]);
		nodes[i].l = n.l;
		nodes[i].r = n.r;
		nodes[i].t = n.t;
	}

	return;
}

void print_node(struct node *node) {
    printf("node: L %d, R %d, T %d\n",
           node->l, node->r, node->t);
    return;
}

void init_ghosts() {
    for (int i = 0, j = 0; i < count; i++) {
        if (nodes[i].t > 0) {
            print_node(&nodes[i]);
            ghosts[j++] = nodes[i];
        }
    }
}

int process_node(struct node node, int ix) {
    if (ix == 0) {
        return node.l;
    }
    else return node.r;
}

int main(int argc, char **argv) {

    printf("Hello, friend\n");
    printf("Advent of code 2021, day 6\n");
    printf("https://adventofcode.com/2021/day/6\n");
    printf("\n");

    if (argc < 2) {
        printf("No file name given\n");
        return -1;
    }

    FILE *fp = fopen(argv[1], "r");

    if (fp == NULL) {
        printf("%s: Can't open file\n", argv[1]);
        exit(1);
    }

    parse_input(fp);

    fclose(fp);

    init_ghosts();

    int nr[6];

    long steps = 0l;

    while (1) {
        for (int i = 0; i < index_count; i++) {
            int ix = indices[i];


            for (int j = 0; j < 6; j++) {
                /* print_node(&ghosts[j]); */
                nr[j] = process_node(ghosts[j], ix);
                /* printf("nr: %d\n", nr[j]); */
            }

            steps++;

            int step_sum = 0;
            for (int j = 0; j < 6; j++) {
                step_sum += ghosts[j].t;
            }

            /* printf("step_sum: %d\n", step_sum); */

            if (step_sum == -6) {
                printf("steps: %ld\n", steps);
                exit(0);
            }

            for (int j = 0; j < 6; j++) {
                ghosts[j] = nodes[nr[j]];
            }
        }
	if (steps % 100000 == 0) {
		printf("steps: %ld\n", steps);
	}
    }

    return 0;
}

