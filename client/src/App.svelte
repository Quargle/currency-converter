<script lang="ts">

	let data:boolean = false; 
	let value:string = '';

	function getCurrencyData() {
		console.log("fetching...");
		fetch("./get_data")
		.then(Response => {
			value = Response.toString();
			data = true;
			})
			.catch(error => {
				console.log(error);
			});
  	}

</script>

<main>
	<h1>Heading</h1>
	<button on:click={getCurrencyData}>Get data</button>
	{#if data}
	<div id="data">
		<p>{value}</p>
	</div>
	{/if}
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>