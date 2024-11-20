<script setup lang="ts">
import { ref } from 'vue'
import {useQuasar} from "quasar";

const $q = useQuasar()

const textfield = ref('')
const textfieldResponse = ref('')
const loading = ref(false)

async function onCheckText() {
  loading.value = true
  const response = await fetch('http://127.0.0.1:5000/api/check-text', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message: textfield.value })
  });

  // Antwort als Text auslesen
  const data = await response.text()
  textfieldResponse.value = data
  loading.value = false
}

function sendMessage() {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard
      .writeText(textfieldResponse.value)
      .then(() => {
        $q.notify({ type: 'positive', message: 'Text kopiert!' });
      })
      .catch((err) => {
        $q.notify({ type: 'negative', message: 'Fehler beim Kopieren' });
        console.error('Clipboard-Fehler:', err);
      });
  } else {
    const textarea = document.createElement('textarea');
    textarea.value = textfieldResponse.value;
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand('copy');
      $q.notify({ type: 'positive', message: 'Text kopiert!' });
    } catch (err) {
      $q.notify({ type: 'negative', message: 'Fehler beim Kopieren' });
      console.error('Fallback-Fehler:', err);
    }
    document.body.removeChild(textarea);
  }
}
</script>

<template>
  <q-page :class="loading ? 'items-center justify-evenly' : 'noCopie'">
    <div class="row q-pa-md">
      <q-editor
        v-model="textfield"
        :toolbar="[]"
        class="full-width"

        :label="!textfield ? 'Gebe hier deinen Text zum überprüfen ein' : 'Dein Text'"
      />

      <div class="full-width flex justify-end">
        <q-btn
        color="secondary"
        label="Überprüfen"
        icon="check"
        :disable="!textfield"
        class="q-mt-md"
        @click="onCheckText"
      >
        <q-tooltip v-if="!textfield">Bitte gebe erst etwas in das Textfeld ein</q-tooltip>
      </q-btn>
      </div>

      <q-btn v-if="textfieldResponse" class="q-mb-xs" size="md" @click="sendMessage" icon="content_copy"></q-btn>
      <q-input v-if="textfieldResponse" v-model="textfieldResponse" class="full-width q-mt-md" filled type="textarea" readonly autogrow />
    </div>

    <q-inner-loading :showing="loading">
      <q-spinner-gears size="50px" color="primary" />
    </q-inner-loading>
  </q-page>
</template>
