export default (
    price: string | number,
    options: Intl.NumberFormatOptions = {
      currency: 'DZD',
      style: 'currency',
    },
  ) => {
    if (typeof price === 'string') price = parseInt(price)
    if (isNaN(price)) price = 0
  
    return new Intl.NumberFormat('dz-DZ', options).format(price)
  }