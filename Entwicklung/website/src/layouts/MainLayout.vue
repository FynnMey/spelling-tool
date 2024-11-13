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

        <div>Fynn Meyer</div>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';

</script>
