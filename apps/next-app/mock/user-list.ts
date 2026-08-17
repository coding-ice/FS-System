const renderUserList = () => {
  return Array.from({length: 10000}, (_, index) => ({
    id: index ,
    name: `User ${index}`,
    email: `user${index}@example.com`,
  }));
};

export default renderUserList;