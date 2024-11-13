<template>
  <q-page class="items-center justify-evenly">
    <div class="row q-pa-md">
      <q-input 
        v-model="textfield" 
        type="textarea" 
        outlined 
        :label="!textfield ? 'Gebe hier deinen Text zum überprüfen ein' : 'Dein Text'" 
        class="col-12"
      />
      <div class="full-width flex justify-end">
        <q-btn 
        color="secondary"
        label="Überprüfen"
        icon="check"
        :disable="textfield ? false : true"
        class="q-mt-md" 
        @click="onCheckText"
      >
        <q-tooltip v-if="!textfield">Bitte gebe erst etwas in das Textfeld ein</q-tooltip>
      </q-btn>
      </div>
      <q-input 
        v-model="textfieldResponse" 
        type="textarea" 
        outlined 
        :label="!textfield ? 'Gebe hier deinen Text zum überprüfen ein' : 'Dein Text'" 
        class="q-mt-md"
      />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';
const textfield = ref('')
const textfieldResponse = ref('')

async function onCheckText() {
  const response = await fetch('/api/check-text', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message: textfield.value }) // Text aus dem Input-Feld senden
    });

    // Antwort als Text auslesen
    const data = await response.text();  // Hier nutzen wir `.text()`, da die Antwort kein JSON ist
    textfieldResponse.value = data

}
</script>
