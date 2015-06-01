Il progetto consiste in un servizio che gestisce una fidelity card centralizzata in comune tra più attività.
Ogni utente ha un account collegato ad un codice (per adesso una stringa casuale).

Questi sono i requisiti:

 - Deve essere possibile iscriversi come attività, inserendo solo i dati di base
 - Deve essere possibile iscriversi come utente, inserendo i dati di base ed indicando se si è in possesso
   di un codice (e in tal caso inserirlo) o meno (dunque generarlo, con la libreria uuid di python)
 - La pagina iniziale deve permetterti di accedere come attività, inserendo utente e password, o come utente
   inserendo solo il codice (no password)
 - L'area riservata dell'impresa deve fare vedere tutti i codici degli utenti associati e permettere di
   aggiungerne altri
 - L'area riservata dell'utente deve far vedere le attività alle quali l'utente è associato
 
Per partire, bisogna creare l'applicazione Django, le varie app, e gli url di base del progetto.

Guardate su myPugliaSOS tutte le parti più difficili come gestione degli utenti, delle registrazioni, login...
NON implementate cose di questo tipo da zero: Django ha già tutto, già testato e perfettamente funzionante.
