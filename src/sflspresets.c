#include <stdio.h>
#include <stdlib.h>

#include <fluidsynth.h>


typedef struct preset_list{
    char name[256];
    struct preset_list *next;
} preset_list_t;

void _preset_list_free(preset_list_t *node) {
    while(node) {
        preset_list_t *next = node->next;
        free(node);
        node = next;
    }
}


preset_list_t *_list_presets(const char *sfpath) {
    // caller must free the strings 
    preset_list_t *preset_list_head = NULL;
    preset_list_t *preset_list_last = NULL;
    const char *adrivers[1] = { NULL };
    fluid_audio_driver_register(adrivers);

    fluid_settings_t *settings = new_fluid_settings();
    fluid_settings_setint(settings, "synth.dynamic-sample-loading", 1);

    fluid_synth_t *sf = new_fluid_synth(settings);
    int id = fluid_synth_sfload(sf, sfpath, 0);
    if (id < 0) {
        fprintf(stderr, "Could not load soundfont\n");
        goto EXIT;
    }
    fluid_sfont_t *sfont = fluid_synth_get_sfont_by_id(sf, id);

    fluid_sfont_iteration_start(sfont);
    int n = 0;
    while(1) {
        fluid_preset_t *preset = fluid_sfont_iteration_next(sfont);
        if(preset == NULL) {
            break;
        }
        preset_list_t *newpreset = malloc(sizeof(preset_list_t));
        newpreset->next = NULL;

        const char *name = fluid_preset_get_name(preset);
        int banknum = fluid_preset_get_banknum(preset);
        int num = fluid_preset_get_num(preset);
        snprintf(newpreset->name, 256, "%03d-%03d %s", banknum, num, name);
        if(preset_list_last != NULL)
            preset_list_last->next = newpreset;
        if (preset_list_head == NULL)
            preset_list_head = newpreset;
        preset_list_last = newpreset;
    }
EXIT:
    free(sf);
    free(settings);
    return preset_list_head;
}
