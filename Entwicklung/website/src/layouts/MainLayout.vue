<script setup lang="ts">
import {Cookies, useQuasar} from "quasar";

const $q = useQuasar()

$q.dark.set(Cookies.get('darkmode') == 'true')
console.log(Cookies.get('darkmode'))

</script>

<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-avatar>
        <img src="/firmen_logo.png">
      </q-avatar>
        <q-toolbar-title>
          Grammify
        </q-toolbar-title>

        <q-btn class="q-mr-md" :icon="$q.dark.isActive ? 'sunny' : 'dark_mode'" flat round @click="() => {
          $q.dark.set(!$q.dark.isActive)
          Cookies.set('darkmode', $q.dark.isActive)
        }" />
        <div>Fynn Meyer</div>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
